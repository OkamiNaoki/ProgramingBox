load ../../CH01_SVD/DATA/allFaces.mat
X = faces;
%% Build Training and Test sets
nTrain = 30; nTest = 20; nPeople = 20;
Train = zeros(size(X,1),nTrain*nPeople);
Test = zeros(size(X,1),nTest*nPeople);
for k=1:nPeople
baseind = 0;
if(k>1) baseind = sum(nfaces(1:k-1));
end
inds = baseind + (1:nfaces(k));
Train(:,(k-1)*nTrain+1:k*nTrain)=X(:,inds(1:nTrain));
Test(:,(k-1)*nTest+1:k*nTest)=X(:,inds(nTrain+1:nTrain+nTest
));
end