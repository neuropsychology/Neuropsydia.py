# -*- coding: utf-8 -*-
import neuropsydia as n


questions_dictionary = {

"Item":{
1:"Neuropsydia is great",
2:"Neuropsydia is not great",
3:"Python is great",
4:"Python is not great"}
,
"Reverse":{
1:False,
2:True,
3:False,
4:True}

}





n.start()
n.questionnaire(questions_dictionary,
                anchors=["No","Yes"],
                results_save=True)
n.close()