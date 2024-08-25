# Use print() to print to the console
a=input()
b=a[::-1]
c=""
for i in b:
  if i=='(':
    c+=')'
  elif i==')':
    c+='('  
  else:
    c+=i
stack=[]
result=""    
precedence={'+':1,'-':1,'*':2,'%':2,'/':2,'^':3}
for i in c:
  if i.isalnum():
    result+=i
  elif i=='(':
    stack.append(i)
  elif i==')':
    while stack and stack[-1]!='(':
      result+=stack.pop()
    stack.pop()
  else:
    if i=='^':
      while stack and stack[-1]!='(' and precedence[i] <= precedence[stack[-1]]:
        result+=stack.pop()
      stack.append(i)
    else:
      while stack and stack[-1]!='(' and precedence[i] < precedence[stack[-1]]:
        result+=stack.pop()
      stack.append(i)
while stack:
  result+=stack.pop()
output=result[::-1]
print(output)