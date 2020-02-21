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
print(['regression-1.png'])
pause
for i = [2:10]
hold off
plot(x,y2,"+r",'linewidth',3)
da=-(y2-(a.*x+b)).*x;
a=a-alpha*mean(da)
db=-(y2-(a.*x+b));
b=b-alpha*mean(db)
y=a*x+b;
hold on
plot(x,y,'linewidth',3)
print(['regression-' num2str(i) '.png'])
pause
end
  
