export default{data(){return{timer:0}},mounted(){setInterval(()=>{this.timer++},1e3)},template:`<div id="timer">
            
        </div>`};