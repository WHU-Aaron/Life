Life myLife = new Life();
myLife.startLife();
while(!myLife.makeSuccess()){
    myLife.tryAgain();
    if(myLife.death())
        break;
}