"""Nyan cat animation frames.
Based on nyan cat animation from http://miku.acm.uiuc.edu/"""

from itertools import cycle


def nyan_animation(rainbow_count=2):
    _ = rainbow_count
    animation = [
        (",,,,,,,,,,,,,,," * _) + ",,,,,,,''''''''''''''',,,,,,,,",
        (">>>>>>>,,,,,,,," * _) + ">>>>>>'@@@@@@@@@@@@@@@',,,,,,,",
        (">>>>>>>>>>>>>>>" * _) + ">>>>>'@@@$$$$$$$$$$$@@@',,,,,,",
        (">>>>>>>>>>>>>>>" * _) + ">>>>>'@@$$$$$-$$-$$$$@@',,,,,,",
        ("&&&&&&&&&&&&&&&" * _) + "&&&&&'@$$-$$$$$$''$-$$@','',,,",
        ("&&&&&&&&&&&&&&&" * _) + "&&&&&'@$$$$$$$$'**'$$$@''**',,",
        ("+++++++&&&&&&&&" * _) + "'''++'@$$$$$-$$'***$$$@'***',,",
        ("+++++++++++++++" * _) + "**''+'@$$$$$$$$'***''''****',,",
        ("+++++++++++++++" * _) + "'**'''@$$$$$$$$'***********',,",
        ("#######++++++++" * _) + "''**''@$$$$$$-'*************',",
        ("###############" * _) + "#''**'@$-$$$$$'***.'****.'**',",
        ("###############" * _) + "##''''@$$$$$$$'***''**'*''**',",
        ("=======########" * _) + "====''@@$$$-$$'*%%********%%',",
        ("===============" * _) + "====='@@@$$$$$$'***''''''**',,",
        (";;;;;;;========" * _) + ";;;;'''@@@@@@@@@'*********',,,",
        (";;;;;;;;;;;;;;;" * _) + ";;;'***''''''''''''''''''',,,,",
        (";;;;;;;;;;;;;;;" * _) + ";;;'**'','*',,,,,'*','**',,,,,",
        (",,,,,,,;;;;;;;;" * _) + ",,,'''',,'',,,,,,,'',,'',,,,,,",

        (",,,,,,,,,,,,,,," * _) + ",,,,,,,''''''''''''''',,,,,,,,,",
        (">>>>>>>,,,,,,,," * _) + ">>>>>>'@@@@@@@@@@@@@@@',,,,,,,,",
        (">>>>>>>>>>>>>>>" * _) + ">>>>>'@@@$$$$$$$$$$$@@@',,,,,,,",
        (">>>>>>>>>>>>>>>" * _) + ">>>>>'@@$$$$$-$$-$$$$@@',,,,,,,",
        ("&&&&&&&&&&&&&&&" * _) + "&&&&&'@$$-$$$$$$$''-$$@',,'',,,",
        ("&&&&&&&&&&&&&&&" * _) + "&&&&&'@$$$$$$$$$'**'$$@','**',,",
        ("+++++++&&&&&&&&" * _) + "+++++'@$$$$$-$$$'***$$@''***',,",
        ("+++++++++++++++" * _) + "+'+++'@$$$$$$$$$'***''''****',,",
        ("+++++++++++++++" * _) + "'*'++'@$$$$$$$$$'***********',,",
        ("#######++++++++" * _) + "'*''''@$$$$$$-$'*************',",
        ("###############" * _) + "#****'@$-$$$$$$'***.'****.'**',",
        ("###############" * _) + "#''**'@$$$$$$$$'***''**'*''**',",
        ("=======########" * _) + "==='''@@$$$-$$$'*%%********%%',",
        ("===============" * _) + "====='@@@$$$$$$$'***''''''**',,",
        (";;;;;;;========" * _) + ";;;;;''@@@@@@@@@@'*********',,,",
        (";;;;;;;;;;;;;;;" * _) + ";;;;'**'''''''''''''''''''',,,,",
        (";;;;;;;;;;;;;;;" * _) + ";;;;'**','*',,,,,,**','**',,,,,",
        (",,,,,,,;;;;;;;;" * _) + ",,,,''',,,'',,,,,,''',,''',,,,,",

        (",,,,,,,>>>>>>>>" * _) + ",,,,,,,,''''''''''''''',,,,,,,,",
        (">>>>>>>>>>>>>>>" * _) + ">>>>>>>'@@@@@@@@@@@@@@@',,,,,,,",
        (">>>>>>>>>>>>>>>" * _) + ">>>>>>'@@@$$$$$$$$$$$@@@',,,,,,",
        ("&&&&&&&&&&&&&&&" * _) + "&&&&&&'@@$$$$$-$$-$$$$@@',,,,,,",
        ("&&&&&&&&&&&&&&&" * _) + "&&&&&&'@$$-$$$$$$$''-$$@',,'',,",
        ("&&&&&&&++++++++" * _) + "&&&&&&'@$$$$$$$$$'**'$$@','**',",
        ("+++++++++++++++" * _) + "++++++'@$$$$$-$$$'***$$@''***',",
        ("+++++++++++++++" * _) + "++++++'@$$$$$$$$$'***''''****',",
        ("+++++++########" * _) + "++++++'@$$$$$$$$$'***********',",
        ("###############" * _) + "#####''@$$$$$$-$'*************'",
        ("###############" * _) + "##'''''@$-$$$$$$'***.'****.'**'",
        ("#######========" * _) + "#'****'@$$$$$$$$'***''**'*''**'",
        ("===============" * _) + "=='''='@@$$$-$$$'*%%********%%'",
        ("=======;;;;;;;;" * _) + "======'@@@$$$$$$$'***''''''**',",
        (";;;;;;;;;;;;;;;" * _) + ";;;;;;''@@@@@@@@@@'*********',,",
        (";;;;;;;;;;;;;;;" * _) + ";;;;;;'*'''''''''''''''''''',,,",
        (";;;;;;;,,,,,,,," * _) + ";;;;;;'**',**',,,,,,**','**',,,",
        (",,,,,,,,,,,,,,," * _) + ",,,,,,''',,''',,,,,,''',,''',,,",

        (",,,,,,,>>>>>>>>" * _) + ",,,,,,,,''''''''''''''',,,,,,,,,",
        (">>>>>>>>>>>>>>>" * _) + ">>>>>>>'@@@@@@@@@@@@@@@',,,,,,,,",
        (">>>>>>>>>>>>>>>" * _) + ">>>>>>'@@@$$$$$$$$$$$@@@',,,,,,,",
        ("&&&&&&&&&&&&&&&" * _) + "&&&&&&'@@$$$$$-$$-$$$$@@',,,,,,,",
        ("&&&&&&&&&&&&&&&" * _) + "&&&&&&'@$$-$$$$$$$''-$$@',,'',,,",
        ("&&&&&&&++++++++" * _) + "&&&&&&'@$$$$$$$$$'**'$$@','**',,",
        ("+++++++++++++++" * _) + "++++++'@$$$$$-$$$'***$$@''***',,",
        ("+++++++++++++++" * _) + "++++++'@$$$$$$$$$'***''''****',,",
        ("+++++++########" * _) + "++++++'@$$$$$$$$$'***********',,",
        ("###############" * _) + "####'''@$$$$$$-$'*************',",
        ("###############" * _) + "##''**'@$-$$$$$$'***.'****.'**',",
        ("#######========" * _) + "##****'@$$$$$$$$'***''**'*''**',",
        ("===============" * _) + "='*'=='@@$$$-$$$'*%%********%%',",
        ("=======;;;;;;;;" * _) + "=='==='@@@$$$$$$$'***''''''**',,",
        (";;;;;;;;;;;;;;;" * _) + ";;;;;;''@@@@@@@@@@'*********',,,",
        (";;;;;;;;;;;;;;;" * _) + ";;;;;'**'''''''''''''''''''',,,,",
        (";;;;;;;,,,,,,,," * _) + ";;;;;'**','*',,,,,,'*','**',,,,,",
        (",,,,,,,,,,,,,,," * _) + ",,,,,''',,,'',,,,,,,'',,''',,,,,",

        (">>>>>>>,,,,,,,," * _) + ">>>>>>>''''''''''''''',,,,,,,,,,",
        (">>>>>>>>>>>>>>>" * _) + ">>>>>>'@@@@@@@@@@@@@@@',,,,,,,,,",
        (">>>>>>>>>>>>>>>" * _) + ">>>>>'@@@$$$$$$$$$$$@@@',,,,,,,,",
        ("&&&&&&&&&&&&&&&" * _) + "&&&&&'@@$$$$$-$$-$$$$@@',,,,,,,,",
        ("&&&&&&&&&&&&&&&" * _) + "&&&&&'@$$-$$$$$$''$-$$@','',,,,,",
        ("+++++++&&&&&&&&" * _) + "+++++'@$$$$$$$$'**'$$$@''**',,,,",
        ("+++++++++++++++" * _) + "+++++'@$$$$$-$$'***$$$@'***',,,,",
        ("+++++++++++++++" * _) + "'''++'@$$$$$$$$'***''''****',,,,",
        ("#######++++++++" * _) + "**''''@$$$$$$$$'***********',,,,",
        ("###############" * _) + "****''@$$$$$$-'*************',,,",
        ("###############" * _) + "''''*'@$-$$$$$'***.'****.'**',,,",
        ("=======########" * _) + "==='''@$$$$$$$'***''**'*''**',,,",
        ("===============" * _) + "====='@@$$$-$$'*%%********%%',,,",
        (";;;;;;;========" * _) + ";;;;''@@@$$$$$$'***''''''**',,,,",
        (";;;;;;;;;;;;;;;" * _) + ";;;''''@@@@@@@@@'*********',,,,,",
        (";;;;;;;;;;;;;;;" * _) + ";;'***'''''''''''''''''''',,,,,,",
        (",,,,,,,;;;;;;;;" * _) + ",,'**','**,,,,,,'**,'**',,,,,,,,",
        (",,,,,,,,,,,,,,," * _) + ",,''',,,'',,,,,,,'',,''',,,,,,,,",

        (">>>>>>>,,,,,,,," * _) + ">>>>>>>''''''''''''''',,,,,,,,,,",
        (">>>>>>>>>>>>>>>" * _) + ">>>>>>'@@@@@@@@@@@@@@@',,,,,,,,,",
        (">>>>>>>>>>>>>>>" * _) + ">>>>>'@@@$$$$$$$$$$$@@@',,,,,,,,",
        ("&&&&&&&&&&&&&&&" * _) + "&&&&&'@@$$$$$-$$''$$$@@','',,,,,",
        ("&&&&&&&&&&&&&&&" * _) + "&&&&&'@$$-$$$$$'**'-$$@''**',,,,",
        ("+++++++&&&&&&&&" * _) + "+++++'@$$$$$$$$'***$$$@'***',,,,",
        ("+++++++++++++++" * _) + "+'+++'@$$$$$-$$'***''''****',,,,",
        ("+++++++++++++++" * _) + "'*'++'@$$$$$$$$'***********',,,,",
        ("#######++++++++" * _) + "'*''''@$$$$$$$'*************',,,",
        ("###############" * _) + "#****'@$$$$$$-'***.'****.'**',,,",
        ("###############" * _) + "#''**'@$-$$$$$'***''**'*''**',,,",
        ("=======########" * _) + "==='''@$$$$$$$'*%%********%%',,,",
        ("===============" * _) + "====='@@$$$-$$$'***''''''**',,,,",
        (";;;;;;;========" * _) + ";;;;''@@@$$$$$$$'*********',,,,,",
        (";;;;;;;;;;;;;;;" * _) + ";;;'*''@@@@@@@@@@''''''''',,,,,,",
        (";;;;;;;;;;;;;;;" * _) + ";;'***''''''''''''''''*',,,,,,,,",
        (",,,,,,,;;;;;;;;" * _) + ",,'**','**,,,,,,'**,'**',,,,,,,,",
        (",,,,,,,,,,,,,,," * _) + ",,''',,''',,,,,,''',,''',,,,,,,,",

        (",,,,,,,,,,,,,,," * _) + ",,,,,,,,''''''''''''''',,,,,,,,,",
        (",,,,,,,>>>>>>>>" * _) + ",,,,,,,'@@@@@@@@@@@@@@@',,,,,,,,",
        (">>>>>>>>>>>>>>>" * _) + ">>>>>>'@@@$$$$$$$$$$$@@@',,,,,,,",
        (">>>>>>>>>>>>>>>" * _) + ">>>>>>'@@$$$$$-$$-$$$$@@',,,,,,,",
        ("&&&&&&&&&&&&&&&" * _) + "&&&&&&'@$$-$$$$$$''$-$$@','',,,,",
        ("&&&&&&&&&&&&&&&" * _) + "&&&&&&'@$$$$$$$$'**'$$$@''**',,,",
        ("&&&&&&&++++++++" * _) + "&'''&&'@$$$$$-$$'***$$$@'***',,,",
        ("+++++++++++++++" * _) + "+'*''+'@$$$$$$$$'***''''****',,,",
        ("+++++++++++++++" * _) + "+'**'''@$$$$$$$$'***********',,,",
        ("+++++++########" * _) + "++'**''@$$$$$$-'*************',,",
        ("###############" * _) + "##''**'@$-$$$$$'***.'****.'**',,",
        ("###############" * _) + "###''''@$$$$$$$'***''**'*''**',,",
        ("#######========" * _) + "#####''@@$$$-$$'*%%********%%',,",
        ("===============" * _) + "======'@@@$$$$$$'***''''''**',,,",
        ("=======;;;;;;;;" * _) + "====='''@@@@@@@@@'*********',,,,",
        (";;;;;;;;;;;;;;;" * _) + ";;;;'***''''''''''''''''''',,,,,",
        (";;;;;;;;;;;;;;;" * _) + ";;;;'**'','*',,,,,'**,'**',,,,,,",
        (";;;;;;;,,,,,,,," * _) + ";;;;'''',,'',,,,,,,'',,'',,,,,,,",

        (",,,,,,,,,,,,,,," * _) + ",,,,,,,,''''''''''''''',,,,,,,,,",
        (",,,,,,,>>>>>>>>" * _) + ",,,,,,,'@@@@@@@@@@@@@@@',,,,,,,,",
        (">>>>>>>>>>>>>>>" * _) + ">>>>>>'@@@$$$$$$$$$$$@@@',,,,,,,",
        (">>>>>>>>>>>>>>>" * _) + ">>>>>>'@@$$$$$-$$-$$$$@@',,,,,,,",
        ("&&&&&&&&&&&&&&&" * _) + "&&&&&&'@$$-$$$$$$$''-$$@',,'',,,",
        ("&&&&&&&&&&&&&&&" * _) + "&&&&&&'@$$$$$$$$$'**'$$@','**',,",
        ("&&&&&&&++++++++" * _) + "&&&&&&'@$$$$$-$$$'***$$@''***',,",
        ("+++++++++++++++" * _) + "++'+++'@$$$$$$$$$'***''''****',,",
        ("+++++++++++++++" * _) + "+'*'++'@$$$$$$$$$'***********',,",
        ("+++++++########" * _) + "+'*''''@$$$$$$-$'*************',",
        ("###############" * _) + "##****'@$-$$$$$$'***.'****.'**',",
        ("###############" * _) + "##''**'@$$$$$$$$'***''**'*''**',",
        ("#######========" * _) + "####'''@@$$$-$$$'*%%********%%',",
        ("===============" * _) + "======'@@@$$$$$$$'***''''''**',,",
        ("=======;;;;;;;;" * _) + "======''@@@@@@@@@@'*********',,,",
        (";;;;;;;;;;;;;;;" * _) + ";;;;;'**'''''''''''''''''''',,,,",
        (";;;;;;;;;;;;;;;" * _) + ";;;;;'**','*',,,,,,**','**',,,,,",
        (";;;;;;;,,,,,,,," * _) + ";;;;;''',,,'',,,,,,''',,''',,,,,",

        (">>>>>>>,,,,,,,," * _) + ">>>>>>>''''''''''''''',,,,,,,,,,",
        (">>>>>>>>>>>>>>>" * _) + ">>>>>>'@@@@@@@@@@@@@@@',,,,,,,,,",
        (">>>>>>>>>>>>>>>" * _) + ">>>>>'@@@$$$$$$$$$$$@@@',,,,,,,,",
        ("&&&&&&&&&&&&&&&" * _) + "&&&&&'@@$$$$$-$$-$$$$@@',,,,,,,,",
        ("&&&&&&&&&&&&&&&" * _) + "&&&&&'@$$-$$$$$$$''-$$@',,'',,,,",
        ("+++++++&&&&&&&&" * _) + "+++++'@$$$$$$$$$'**'$$@','**',,,",
        ("+++++++++++++++" * _) + "+++++'@$$$$$-$$$'***$$@''***',,,",
        ("+++++++++++++++" * _) + "+++++'@$$$$$$$$$'***''''****',,,",
        ("#######++++++++" * _) + "#####'@$$$$$$$$$'***********',,,",
        ("###############" * _) + "####''@$$$$$$-$'*************',,",
        ("###############" * _) + "#'''''@$-$$$$$$'***.'****.'**',,",
        ("=======########" * _) + "'****'@$$$$$$$$'***''**'*''**',,",
        ("===============" * _) + "='''='@@$$$-$$$'*%%********%%',,",
        (";;;;;;;========" * _) + ";;;;;'@@@$$$$$$$'***''''''**',,,",
        (";;;;;;;;;;;;;;;" * _) + ";;;;;''@@@@@@@@@@'*********',,,,",
        (";;;;;;;;;;;;;;;" * _) + ";;;;;'*'''''''''''''''''''',,,,,",
        (",,,,,,,;;;;;;;;" * _) + ",,,,,'**',**',,,,,,**'.'**',,,,,",
        (",,,,,,,,,,,,,,," * _) + ",,,,,''',,''',,,,,,''',,''',,,,,",

        (">>>>>>>,,,,,,,," * _) + ">>>>>>>''''''''''''''',,,,,,,,,,",
        (">>>>>>>>>>>>>>>" * _) + ">>>>>>'@@@@@@@@@@@@@@@',,,,,,,,,",
        (">>>>>>>>>>>>>>>" * _) + ">>>>>'@@@$$$$$$$$$$$@@@',,,,,,,,",
        ("&&&&&&&&&&&&&&&" * _) + "&&&&&'@@$$$$$-$$-$$$$@@',,,,,,,,",
        ("&&&&&&&&&&&&&&&" * _) + "&&&&&'@$$-$$$$$$$''-$$@',,'',,,,",
        ("+++++++&&&&&&&&" * _) + "+++++'@$$$$$$$$$'**'$$@','**',,,",
        ("+++++++++++++++" * _) + "+++++'@$$$$$-$$$'***$$@''***',,,",
        ("+++++++++++++++" * _) + "+++++'@$$$$$$$$$'***''''****',,,",
        ("#######++++++++" * _) + "#####'@$$$$$$$$$'***********',,,",
        ("###############" * _) + "###'''@$$$$$$-$'*************',,",
        ("###############" * _) + "#''**'@$-$$$$$$'***.'****.'**',,",
        ("=======########" * _) + "=****'@$$$$$$$$'***''**'*''**',,",
        ("===============" * _) + "'*'=='@@$$$-$$$'*%%********%%',,",
        (";;;;;;;========" * _) + ";';;;'@@@$$$$$$$'***''''''**',,,",
        (";;;;;;;;;;;;;;;" * _) + ";;;;;''@@@@@@@@@@'*********',,,,",
        (";;;;;;;;;;;;;;;" * _) + ";;;;'**'''''''''''''''''''',,,,,",
        (",,,,,,,;;;;;;;;" * _) + ",,,,'**','*',,,,,,**','**',,,,,,",
        (",,,,,,,,,,,,,,," * _) + ",,,,''',,,'',,,,,,''',,''',,,,,,",

        (",,,,,,,>>>>>>>>" * _) + ",,,,,,,,''''''''''''''',,,,,,,,,",
        (">>>>>>>>>>>>>>>" * _) + ">>>>>>>'@@@@@@@@@@@@@@@',,,,,,,,",
        (">>>>>>>>>>>>>>>" * _) + ">>>>>>'@@@$$$$$$$$$$$@@@',,,,,,,",
        ("&&&&&&&&&&&&&&&" * _) + "&&&&&&'@@$$$$$-$$-$$$$@@',,,,,,,",
        ("&&&&&&&&&&&&&&&" * _) + "&&&&&&'@$$-$$$$$$''$-$$@','',,,,",
        ("&&&&&&&++++++++" * _) + "&&&&&&'@$$$$$$$$'**'$$$@''**',,,",
        ("+++++++++++++++" * _) + "++++++'@$$$$$-$$'***$$$@'***',,,",
        ("+++++++++++++++" * _) + "+'''++'@$$$$$$$$'***''''****',,,",
        ("+++++++########" * _) + "'**''''@$$$$$$$$'***********',,,",
        ("###############" * _) + "'****''@$$$$$$-'*************',,",
        ("###############" * _) + "#''''*'@$-$$$$$'***.'****.'**',,",
        ("#######========" * _) + "####'''@$$$$$$$'***''**'*''**',,",
        ("===============" * _) + "======'@@$$$-$$'*%%********%%',,",
        ("=======;;;;;;;;" * _) + "=====''@@@$$$$$$'***''''''**',,,",
        (";;;;;;;;;;;;;;;" * _) + ";;;;''''@@@@@@@@@'*********',,,,",
        (";;;;;;;;;;;;;;;" * _) + ";;;'***'''''''''''''''''''',,,,,",
        (";;;;;;;,,,,,,,," * _) + ";;;'**'''***,,,,,'**''**',,,,,,,",
        (",,,,,,,,,,,,,,," * _) + ",,,''',,,'',,,,,,,''',''',,,,,,,",

        (",,,,,,,>>>>>>>>" * _) + ",,,,,,,,''''''''''''''',,,,,,,,,",
        (">>>>>>>>>>>>>>>" * _) + ">>>>>>>'@@@@@@@@@@@@@@@',,,,,,,,",
        (">>>>>>>>>>>>>>>" * _) + ">>>>>>'@@@$$$$$$$$$$$@@@',,,,,,,",
        ("&&&&&&&&&&&&&&&" * _) + "&&&&&&'@@$$$$$-$$''$$$@@','',,,,",
        ("&&&&&&&&&&&&&&&" * _) + "&&&&&&'@$$-$$$$$'**'-$$@''**',,,",
        ("&&&&&&&++++++++" * _) + "&&&&&&'@$$$$$$$$'***$$$@'***',,,",
        ("+++++++++++++++" * _) + "++'+++'@$$$$$-$$'***''''****',,,",
        ("+++++++++++++++" * _) + "+'*'++'@$$$$$$$$'***********',,,",
        ("+++++++########" * _) + "+'*''''@$$$$$$$'*************',,",
        ("###############" * _) + "##****'@$$$$$$-'***.'****.'**',,",
        ("###############" * _) + "##''**'@$-$$$$$'***''**'*''**',,",
        ("#######========" * _) + "####'''@$$$$$$$'*%%********%%',,",
        ("===============" * _) + "======'@@$$$-$$$'***''''''**',,,",
        ("=======;;;;;;;;" * _) + "=====''@@@$$$$$$$'*********',,,,",
        (";;;;;;;;;;;;;;;" * _) + ";;;;'*''@@@@@@@@@@''''''''',,,,,",
        (";;;;;;;;;;;;;;;" * _) + ";;;'***''''''''''''''''*',,,,,,,",
        (";;;;;;;,,,,,,,," * _) + ";;;'**','**,,,,,,'**''**',,,,,,,",
        (",,,,,,,,,,,,,,," * _) + ",,,''',,''',,,,,,''',,''',,,,,,,",
    ]
    return animation


def infinite_nyan(rainbow_count=2):
    return cycle(nyan_animation(rainbow_count))
