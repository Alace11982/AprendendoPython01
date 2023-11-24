# Correspondendo a zero ou mais ocorrências usando asterisco
import re

batRegex = re.compile(r"Bat(wo)*man")
mo1 = batRegex.search("The Adventures of Batman")
print(mo1.group())

mo2 = batRegex.search("The Adventures of Batwoman")
print(mo2.group())

mo3 = batRegex.search("The Adventures do Batwowowowowowowowoman")
print(mo3.group())
