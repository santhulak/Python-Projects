from deep_translator import GoogleTranslator
input= 'Three hundred eighty-one meters, 102 floors, and 6,500 windows. We know that more than 2.5 million people visit the Empire State Building each year. An average of eighty-seven couples get engaged atop its observatory every month.'
output = GoogleTranslator(source='auto', target='ta').translate(input)
print(output)
