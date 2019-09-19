alias="test"
port=1111
echo $alias
ssh -o "StrictHostKeyChecking no"  -R $alias:$port:localhost:22 teleport.anhdh.com
