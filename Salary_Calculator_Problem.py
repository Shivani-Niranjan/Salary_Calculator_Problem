sun, mon, tue, wed, thur, fri, sat = map(int, input().split())
salary = 0
sun = sun*150
mon = (mon*100 if mon<=8 else (8*100)+((mon - 8)*115))
tue = (tue*100 if tue<=8 else (8*100)+((tue - 8)*115))
wed = (wed*100 if wed<=8 else (8*100)+((wed - 8)*115))
thur = (thur*100 if thur<=8 else (8*100)+((thur - 8)*115))
fri = (fri*100 if fri<=8 else (8*100)+((fri - 8)*115))
sat = sat * 125
print(sun+ mon+ tue+ wed+ thur+ fri+ sat)