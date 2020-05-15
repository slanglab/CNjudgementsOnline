import pandas as pd
import numpy as np
import re

def extractAlcoholNumber(df):
    facts = df['fact'].tolist()
    results = []
    notes = []
    noMatchCount = 0
    multipleMatchesCount = 0
    parseNumErrorCount = 0
    firstHalfMatchCount = 0
    
    for fact in facts:
#         match = re.search(r'\d*.\d*mg／100ml',fact)
        fact = fact.replace('\n', ' ').replace('\r', '')
        matchall = re.findall(u'\d+(?:.|．)?\d*\(*(?:mg|MG|㎎|毫克|Mg|mG|mmg)(?:/|／)(?:100|lOO)(?:ml|ML|m1|mL|dL|毫升|Ml)\)*', fact, re.UNICODE)
        note=None
        if not matchall:
#             print('match empty')
#             print(fact)
            matchall = re.findall(u'\d+(?:.|．)?\d*\(*(?:mg|MG|㎎|毫克|Mg|mG|mmg)\)*', fact, re.UNICODE)
            if not matchall:
                results.append(None)
                notes.append('noMatch') 
                noMatchCount += 1
                continue
            else:
                if not note:
                    note = 'firstHalfMatch'
                firstHalfMatchCount += 1
#                 print('firstHalfMatch')
#                 print(fact)
            
        if len(matchall) > 1:
#             print('multiple matches')
#             print(fact)
              multipleMatchesCount += 1
              if not note:
                  note='multipleMatches'
        else:
            if not note:
                note = 'oneMatch'

        nums = []
        try:
            for x in matchall:
                x = x.replace('(', '')
                if 'mmg' in x:
                    numstr = x.split('mmg')[0]
                elif 'mg' in x:
                    numstr = x.split('mg')[0]
                elif 'MG' in x:
                    numstr = x.split('MG')[0]
                elif '㎎' in x:
                    numstr = x.split('㎎')[0]
                elif '毫克' in x:
                    numstr = x.split('毫克')[0]
                elif 'Mg' in x:
                    numstr = x.split('Mg')[0]
                elif 'mG' in x:
                    numstr = x.split('mG')[0]
                
                if "．" in numstr:
                    numstr = numstr.replace('．', '.')
                
                num = float(numstr)
                nums.append(num)
                
        except:
#             print('error:')
#             print(fact)
            results.append(-10)
            notes.append('parseError')   
            parseNumErrorCount += 1
            continue      
            
        bloodAlcohol = max(nums)
        results.append(bloodAlcohol)
        notes.append(note)
            
    return (results, notes, noMatchCount, multipleMatchesCount,parseNumErrorCount, firstHalfMatchCount)

        
