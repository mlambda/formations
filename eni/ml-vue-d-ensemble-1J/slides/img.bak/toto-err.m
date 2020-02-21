alpha=0.01
a=0.58961
b=0.25849
x=[0:10];
y2=[-2.1978 6.3698 5.7063 13.2279 10.1201 19.3790 19.2189 23.4135 27.3058 26.4152 32.2293];
hold off
plot(x,y2,"+r",'linewidth',3)
hold on
y=a*x+b;
plot(x,y,'linewidth',3)
for i = [0:10]
u=[i i];
v=[y(i+1) y2(i+1)];
plot(u,v,"-g",'linewidth',3)
end
print('regression-error.png')
  
