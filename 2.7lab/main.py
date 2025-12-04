def merge_files(file1_path, file2_path, output_path):  
    # Открываем оба файла для чтения  
    with open(file1_path, 'r', encoding='utf-8') as file1, \  
         open(file2_path, 'r', encoding='utf-8') as file2:  
          
        # Читаем все строки из обоих файлов  
        lines1 = file1.readlines()  
        lines2 = file2.readlines()  
          
        # Открываем файл для записи результата  
        with open(output_path, 'w', encoding='utf-8') as output:  
            # Проходим по строкам первого файла  
            for i in range(len(lines1)):  
                # Добавляем строку из второго файла, если она есть  
                if i < len(lines2):  
                    # Убираем символ новой строки из второй строки  
                    # и добавляем её к первой строке  
                    output.write(lines1[i].rstrip('\n') + lines2[i])  
                else:  
                    # Если строк во втором файле нет, просто копируем первую строку  
                    output.write(lines1[i])  
