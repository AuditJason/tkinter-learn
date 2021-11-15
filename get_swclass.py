#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from openpyxl import load_workbook
from copy import deepcopy


class SwClass:
    @property
    def swclass(self):
        html_doc = open('SwClass.xls', 'r', encoding='GBK').read()
        soup = BeautifulSoup(html_doc, "html.parser")
        td = soup.find_all('td')
        industry = {}
        industry_company = {}
        for i in range(len(td)//5):
            indus = td[i*5].string
            code = td[i*5+1].string
            name = td[i*5+2].string
            if indus in industry_company.keys():
                industry_company[indus].append([code, name])
            else:
                industry_company[indus] = [[code, name]]
                industry[indus] = None
        return industry_company, industry

    @property
    def swclass_all(self):
        wb = load_workbook('../valuerdataget/SwClass/最新个股申万行业分类(完整版-截至7月末).xlsx')
        sheet = wb.worksheets[0]
        # 添加类key的另一种方式。创建三级行业dict,最后不包含公司。
        industry_class_all2 = {}
        for row in sheet.rows:
            vs = [v.value for v in row]
            type_exchange = vs[0]
            if type_exchange == 'A股':
                industry_id = vs[1]
                stock_id = vs[2]
                stock_name = vs[3]
                class1 = vs[4]
                class2 = vs[5]
                class3 = vs[6]

                if class1 not in industry_class_all2:
                    industry_class_all2[class1] = {}

                if class2 not in industry_class_all2[class1]:
                    industry_class_all2[class1][class2] = {}

                if (industry_id, class3) not in industry_class_all2[class1][class2]:
                    industry_class_all2[class1][class2][(industry_id,class3)] = []

        industry_company = deepcopy(industry_class_all2)
        for row in sheet.rows:
            vs = [v.value for v in row]
            type_exchange = vs[0]
            if type_exchange == 'A股':
                industry_id = vs[1]
                stock_id = vs[2]
                stock_name = vs[3]
                class1 = vs[4]
                class2 = vs[5]
                class3 = vs[6]
                industry_company[class1][class2][(industry_id, class3)].append((stock_id, stock_name))
        return industry_class_all2, industry_company
