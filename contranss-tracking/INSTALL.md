sudo npm install mosca bunyan -g
mosca -v --host 0.0.0.0 --http-port 3000 --http-bundle --http-static ./ | bunyan