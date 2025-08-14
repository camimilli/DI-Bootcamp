import os 
from translate import Translator 

translator = Translator(to_lang="ja")

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(f'{dir_path}/test.txt', 'r', encoding='utf-8') as file_en:
    to_translate = file_en.read()
    translated_text = translator.translate(to_translate)
    with open('./test-ja.txt', mode='w') as my_file:
        my_file.write(translated_text)
        print("'/test.txt' was created succesfully")
   
