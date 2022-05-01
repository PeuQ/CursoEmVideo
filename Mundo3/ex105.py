# make a function that receives various scores from students and return the following dictionary: {how many scores were received, highest score, lowest score, class avarage score, situation(optional)}

#function def:
def class_score(*scores, situation=False): #situation default set for False
  dict = {'quantity': len(scores), 'highest': max(scores), 'lowest': min(scores), 'avarage': sum(scores)/len(scores)}

  if situation:
    if dict['avarage'] >= 7.0:
      dict['situation'] = 'GOOD'
    if dict['avarage'] >= 5.0:
      dict['situation'] = 'REASONABLE'
    else:
      dict['situation'] = 'BAD'
  
  return dict
  
#main
final_result = class_score(8,9,4,2,6,7,3)
print(final_result)
print("\n\n")
final_result = class_score(3,4,5,6, situation=True)
print(final_result)
