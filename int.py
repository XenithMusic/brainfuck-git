e=exec
v=eval
s=str
z=lambda a:e("r"+s(r)+a)
with open("f","r") as f:
 k=[];d=f.read();r=0;c=0;o=""
 while c<(len(d)):
  i=d[c]
  if not "r"+s(r) in locals(): z("=0")
  if i in["+","-"]:z(i+"=1")
  if i=="<":r -= 1
  if i==">":r += 1
  if i==".":e("o+='"+chr(v("r"+s(r)))+"'");
  if i==",":z("=ord('"+input(">")[0]+"')")
  if i=="[":k=k+[c]
  if i=="]":
   x=v("r"+s(r))!=0
   if x:c=k[-1]
   if not x:k=k[:-1]
  c+=1
print(o)
