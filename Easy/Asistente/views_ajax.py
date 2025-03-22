from  google import genai

from django.http import JsonResponse
from datetime import datetime
from . import models
from django.db.models import Q
from Caja.models import  Movements
from Company.models import Company
from Client.models import Client
from Credit.models import Credit, Cuotas


def CleanQuestion(question, request):

      if any(word in question.lower() for word in ['client', 'cedula', 'numero']):
            clientes = Client.objects.filter(company=request.user.more.company).order_by('-id')[:50]
            client_data = []
            for cliente in clientes:
                  client_data.append({
                        'name': cliente.name if cliente.name else 'N/A',
                        'last_name': cliente.last_name,
                        'cedula': cliente.dni ,
                        'numero': cliente.phone,
                        'correo': cliente.email,
                  })
            return f'{client_data}'
      
      elif any(word in question.lower() for word in ['prestam', 'credit', 'cuota']):
            creditos = Credit.objects.filter(is_active=True,
            company=request.user.more.company).order_by('-id')[:50]
            creditos_data = []
            for s in creditos:
                  creditos_data.append({
                              'nombre_de_cliente': s.client.name if s.client.name else 'N/A',
                              'apellido_de_cliente': s.client.last_name if s.client.last_name else 'N/A',
                              'cedula_de_cliente': s.client.dni if s.client.dni else 'N/A',
                              'payment': s.payment if 'Si' else 'No',
                              'capital_prestado': s.capital,
                              'cantidad_de_cuotas': s.cuotas,
                              'intereses': s.intereses,
                              'frecuencia_de_pago': s.frecuencia,
                              'dia_de_pago': s.day_pay,
                              'tipo_de_prestamo_o_metodo': s.metodo,
                              'cuotas_pagadas': Cuotas.objects.filter(credit=s, payment=True).count(),
                              'cuotas_sin_pagar': Cuotas.objects.filter(credit=s, payment=False).count()
                  })
            return creditos_data if creditos_data else 'No hay prestamos en mi lista'

      else:
            return 'Solo puedo responder preguntas sobre clientes, creditos, agendas, caja, inversiones, calculadora, ubicaciones, empresas'
      
      

def QuestionGemini(request):
      your_question  = request.GET.get('question')
      data = {'data': False}
      if your_question:
            client = genai.Client(api_key="AIzaSyAlRiEbU6bhninS9aZvaO5MfB8jWyzfjw0")
            asisten_response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents = f"""
                    Sistema: Easy
                    Contexto: Easy es un asistente virtual para la gestión de un software financiero, proporcionando respuestas precisas y detalladas.
                    Objetivo: Proporcionar información específica y actualizada sobre clientes, creditos, agendas, inversiones y otros aspectos relacionados con la gestión de la financiera.
                    Fecha actual: {datetime.now().strftime('%d/%m/%Y')}
                    Pregunta del usuario: {your_question}
                    Información adicional: {CleanQuestion(your_question, request)}
                    """,)
            
            if your_question:
                  data = {
                        'your_question': your_question,
                        'asistent_response': asisten_response.text if asisten_response.text else 'No se encontró respuesta'
                  }
      return JsonResponse(data)