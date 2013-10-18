var xmlhttp;
xmlhttp = new XMLHttpRequest();
xmlhttp.open("GET", "http://reddit.com/r/borderlands2/.json", true);
xmlhttp.send()
document.write('Hello Javascript');