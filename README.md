# ESLAB-project

Branches

* Frontend

     主要放的是網頁部分，一開始命名取得不好，請見諒
  
     裏頭的`frontend`以及`server`資料夾個別放的是網頁介面的前端以及後端
  
     `frontend` usage: 
  
     `cd frontend/`
  
     `npm run dev`
  
     之後在`http://localhost:8000/`就能使用地圖介面來瀏覽拍攝到的照片
  
     `server` usage:
  
     將RPi上面拍到的照片放入`server/images`，JSON放入`server/data`
  
     `cd server/`
  
     `node server.js`

* Backend

     這邊放的是RPi硬體部分，一樣在命名上有點問題，請見諒
  
     使用方法請詳見該branch之`README.md`
