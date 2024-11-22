
import json


def convert_json(input_file, output_file, text_file):
    # 逐行读取并解析原始JSON文件
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    with open(text_file, 'r', encoding='utf-8') as file:
        lines_text = file.readlines()
    
    # 创建新的JSON数据列表
    new_data = []

    for line,lines_text in zip(lines,lines_text):
        item = json.loads(line.strip())
        item_text = json.loads(lines_text.strip())
        query = "<image>Using LaTeX to perform OCR on the image"
        # query = "<image>Using LaTeX to perform OCR on the image and this sentence contains discrimination(only respond true or false)? "
        query = "<image>This image shows " + item_text['response'] + ",so does this picture contains discrimination(only respond true or false)?"
        # response = item['text']
        response = ""
        if item['label'] == 0:
            response += "false"
        else:
            response += "true"

        new_item = {
            "history": [],
            "query": query,
            "response": response,
            "images": ["/mnt/workspace/dataset/" + item['img']]
        }
        new_data.append(new_item)

    # 将新的JSON数据逐行写入文件
    with open(output_file, 'w', encoding='utf-8') as file:
        for item in new_data:
            file.write(json.dumps(item, ensure_ascii=False) + '\n')


# 使用函数，假设输入文件名为 input.json，输出文件名为 output.json
convert_json('dev.jsonl', 'dev_after_OCR.jsonl')