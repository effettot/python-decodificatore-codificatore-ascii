import base64

# Codifica una stringa in Base64
message = "Ciao, come stai?"
message_bytes = message.encode('ascii')
base64_bytes = base64.b64encode(message_bytes)
base64_message = base64_bytes.decode('ascii')

print("Messaggio codificato in Base64:", base64_message)

# Decodifica il messaggio in Base64
decoded_bytes = base64.b64decode(base64_message)
decoded_message = decoded_bytes.decode('ascii')

print("Messaggio decodificato:", decoded_message)
