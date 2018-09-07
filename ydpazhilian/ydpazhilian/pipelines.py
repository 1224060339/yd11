# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class YdpazhilianPipeline(object):
    def process_item(self, item, spider):
        """
        保存到JSON文件中
        """
        with open("zhilian.json", 'ab') as f:
            #以json字典的形式写入文件
            text = json.dumps(dict(item), ensure_ascii=False)+'\n'
            f.write(text.encode('utf-8'))
        
        return item
