# new update :a shield is rotating 
import os
print("""<!DOCTYPE html>
<html lang="en">
<head>
<title>Captain America Shield</title>
</head>
<div class="container">
<div class="circle outer-lv3">
<div class="circle outer-lv2">
<div class="circle outer-lv1">
<div class="center">
<div class="arrow top"></div>
<div class="arrow left"></div>
<div class="arrow right"></div>
</div>
</div>
</div>
</div>
</div>
<style>
html, body {
background:#000000;
height: 500px;
}
.container {
width:100%;
height: 100%;
display: flex;
justify-content: center;
align-items: center;
}
.circle {
border-radius: 50%;
display: flex;
flex-direction: row;
justify-content: center;
align-items: center;
border:1px solid #000;
}
.outer-lv3 {
background-image: linear-gradient(#870000,#870000,#870000);
height: 260px;
width: 260px;
-webkit-animation: turning 8s infinite linear;
animation: turning 8s infinite linear;
}

.outer-lv2 {
background: #a5a5ab;
background-image: linear-gradient(#a5a5ab,#a5a5ab,#a5a5ab);
height: 210px;
width: 210px;
}@-webkit-keyframes turning {
20% {transform: rotate(0deg)}
100% {transform: rotate(360deg)}
}
@keyframes turning {
20% {transform: rotate(0deg)}
100% {transform: rotate(360deg)}
}
.outer-lv1 {
background-image: linear-gradient(#870000 ,#870000,#870000);
height: 150px;
width: 150px;
}
.center {
background-image: linear-gradient(#000042,#000042,#000042);
height: 100px;
width: 100px;
border-radius: 50%;
position: relative;
overflow: hidden;
border:1px solid #000042;
}
.arrow {
border-top: 35px solid #a5a5ab;
border-bottom: 48px solid rgba(0,0,0,0.0);
border-left: 48px solid transparent;
border-right: 48px solid transparent;
position: absolute;
height: 0;
width: 0;
}
.top {
top: 35px;
left: 2px;
}
.left {
transform: rotate(72deg);
top: 16px;
left: -24px;
}
.right {
transform: rotate(-72deg);
top: 16px;
left: 25px;
}
</style>
</body>
</html> """)
#i need (+1000 upvotes) in this code.thani made it more awosome
__import__("os").system("touch trick.png")

