python .\manage.py makemigrations
python .\manage.py migrate

cd .\frontend\
npm init -y
npm i webpack webpack-cli --save-dev

npm i @babel/core babel-loader @babel/preset-env @babel/preset-react --save-dev

npm i react react-dom --save-dev

npm i @material-ui/core --force (no react17.0 support)

npm i @babel/plugin-proposal-class-properties (concurrency)

npm i react-router-dom

npm i @material-ui/icons --force

npm install @types/react @types/react-dom