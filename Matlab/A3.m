M = rand(3) 
ColSum = sum(M,1) 
M(:,1) = M(:,1) / ColSum(1) 
M(:,2) = M(:,2) / ColSum(2)
M(:,3) = M(:,3) / ColSum(3)
M
M=[0 1 0 0 0;0 0 1 0 0;0 0 0 1 0;0 0 0 0 1;1 0 0 0 0]
[ V E ] = eig(M)
s= [ 1 0 0 0 0 ]'
for i=1:100
s = M*s;
end

for i=1:3
s'*V(:,i) / ( norm(s) * norm( V(:,i) ) )
end