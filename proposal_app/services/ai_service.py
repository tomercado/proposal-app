import requests
import json
import re

OLLAMA_API_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3.2"

SYSTEM_PROMPT = """
Actúa como un asesor comercial senior experto en redacción de cotizaciones formales para clientes empresariales en Colombia.

Tu tarea es:
- Corregir redacción, ortografía y estilo.
- Mejorar la presentación y el orden del texto.
- Hacer el lenguaje más profesional, claro y elegante.
- Mantener un tono respetuoso, formal y comercial.

REGLAS CRÍTICAS (OBLIGATORIAS):
1. NO inventes precios, descuentos, cantidades, condiciones ni productos.
2. NO modifiques ningún número, valor, unidad, cantidad o precio.
3. NO completes información que no esté explícitamente en el texto original.
4. NO interpretes ni asumas condiciones comerciales.
5. Si una información está incompleta o es confusa, déjala tal como está, solo mejorando la redacción.
6. Está PROHIBIDO agregar frases como “entrega rápida”, “si paga rápido”, “promociones especiales” u otras similares si no están en el texto original.
7. Mantén exactamente los mismos productos y valores, solo reescribiendo el texto.

FORMATO deseado en el cuerpo del texto:
- Saludo formal: “Estimado señor,” o “Estimado(a) señor(a),”.
- Texto organizado por secciones y listas claras.
- Cierre formal y profesional.

IMPORTANTE:
Si cambias, inventas o alteras cualquier número, el resultado será inválido.

FORMATO JSON OBLIGATORIO DE SALIDA (Para poder procesarlo):
{
    "cliente": "Nombre del cliente detectado",
    "titulo": "Título de la propuesta",
    "introduccion": "Saludo y párrafo introductorio",
    "cuerpo": "El contenido completo de los productos y precios ya corregido y organizado."
}
"""

def organize_proposal_data(raw_text):
    """
    Envía el texto crudo a Ollama y retorna un diccionario estructurado.
    """
    full_prompt = f"{SYSTEM_PROMPT}\n\nTEXTO A CORREGIR:\n{raw_text}\n\nSALIDA JSON:"
    
    payload = {
        "model": MODEL_NAME,
        "prompt": full_prompt,
        "format": "json",  # Forzamos salida JSON
        "stream": False,
        "options": {
            "temperature": 0.2 
        }
    }
    
    try:
        response = requests.post(OLLAMA_API_URL, json=payload, timeout=60)
        response.raise_for_status()
        result_text = response.json().get('response', '')
        
        return parse_ai_response(result_text)
        
    except requests.exceptions.ConnectionError:
        return {"error": "No se pudo conectar con Ollama. Asegúrate de que esté corriendo en localhost:11434"}
    except Exception as e:
        return {"error": f"Error procesando la IA: {str(e)}"}

def parse_ai_response(text):
    """
    Parsea el JSON de la IA.
    """
    data = {
        "error": None,
        "title": "",
        "client_name": "",
        "intro_text": "",
        "content": ""
    }

    try:
        # Intentar limpiar el texto por si la IA añade algo antes o después del JSON
        json_match = re.search(r'\{.*\}', text, re.DOTALL)
        if json_match:
            json_str = json_match.group(0)
            parsed = json.loads(json_str)
            
            data["title"] = parsed.get("titulo", "Propuesta Comercial")
            data["client_name"] = parsed.get("cliente", "")
            data["intro_text"] = parsed.get("introduccion", "")
            data["content"] = parsed.get("cuerpo", "")
        else:
            # Fallback simple si no hay JSON
            data["content"] = text
            data["intro_text"] = "Estimado cliente,"
            
    except json.JSONDecodeError:
        data["content"] = text # Si falla, devolver todo en el contenido
        
    return data
