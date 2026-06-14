@echo off
echo "=== DEPLOYMENT ==="
kubectl get deployment nginx-deployment -o wide

echo.
echo "=== REPLICASET (managed by Deployment) ==="
kubectl get rs -l app=nginx -o wide 

echo.
echo "=== PODS (managed by ReplicaSet) ==="
kubectl get pods -l app=nginx -o wide

echo.
echo "=== OWNERSHIP CHAIN ==="
kubectl get pods -l app=nginx -o jsonpath='{range.items[*]}{.metadata.ownerReferences}'
::kubectl get pods -o jsonpath='{range.items[*]}{.metadata.ownerReferences}'
@echo on
pause