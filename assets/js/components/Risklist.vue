<template>
    <div class="main">
        <div class="position">
            <div class="list">
                <h2 class="i-title">RISK TYPES</h2>
                <ul>
                    <li v-for="risk in risks"><button :id="risk.id" v-on:click="showmsg" class="risk-item">{{ risk.title }}</button></li>
                </ul>
            </div>
            <div class="detail">
                <h2 class="i-title">{{ risky.title }}</h2>
                <span class="description">{{ risky.description }}</span>
                
                <form method='POST'>
                    <div v-if="risky.empty">Please Select a Risk type to continue</div>
                    <div v-else>
                        <ul>
                            <li v-for="field in risky.fields" id="fld">
                                <div v-if="field.type === 'enum'">
                                    <label>{{ field.title }}</label>
                                    <select :name="field.name">
                                        <option v-for="choice in field.choices" :value="choice">{{choice}}</option>
                                    </select>
                                </div>
                                
                                <div v-else-if="field.type === 'date'">
                                    <label>{{field.title}}</label>
                                    <date-picker v-model="time1" :first-day-of-week="1" lang="en" id="date"></date-picker>
                                </div>
                                
                                <div v-else>
                                    <label>{{field.title}}</label>
                                    <input :type="field.type" :name="field.name" />
                                </div>
                            </li>
                        </ul>
                        <div class="sub">
                            <button type="button" class="submit">Submit</button>
                        </div>
                    </div>
                </form>
                
            </div>
        </div>
    </div>
    
</template>

<script>
import DatePicker from 'vue2-datepicker';
var axios = require('axios');

    export default{
        name:'risklist',
        data: function(){
            return{
                risks:[],
                risky:{'empty':true},
                time1: '',
                time2: '',
                shortcuts: [
                    {
                    text: 'Today',
                    start: new Date(),
                    end: new Date()
                    }
                ]
            };
        },
        
        components:{ DatePicker },
        
        created:function(){
              var vm = this;
              axios.get('https://cmbd5dg374.execute-api.us-east-2.amazonaws.com/dev/core/risk/all/')
                .then(function(response){
                    vm.risks = response.data;
                });
          },
           
        methods:{
           showmsg:function(e){
              var mv = this;
              axios.get('https://cmbd5dg374.execute-api.us-east-2.amazonaws.com/dev/core/risk/' + e.target.id + '/')
                .then(function(response){
                    mv.risky = response.data;
                });
           }
       }
    };
</script>

<style scoped>

.main{
    width:100%;
    height:100%;
}

.position{
    margin-top:10px;
    min-height:100%;
    display:block;
}

.list{
    min-width:30%;
    min-height: 572px;
    float:left;
    background:rgba(68,68,68,0.3);
    color:#fff;
    border-radius:0px 0px 0px 20px;
}

.detail{
    min-width:70%;
    min-height: 572px;
    float:left;
    background:rgba(247,247,247, 0.2);
    color:#ECEFF1;
    border-radius:0px 0px 20px 0px;
}

.i-title{
    text-align:center;
    color:#ECEFF1;
}

ul{
    padding:15px;
}

li{
    list-style-type:None;
}

.risk-item{
    min-width:100%;
    max-width:100%;
    min-height:40px;
    max-height:40px;
    margin-bottom:10px;
    margin-right:10px;
    border-radius:5px;
    border:0.5px solid #fff;
}

.risk-item{
    color:#7986cb;
    background:#37474f;
    font-size:1.2em;
    text-transform:capitalize;
}

.risk-item:hover{
    border-color: #21333C;
    background-color: #21333C;
    color:#fff;
}

.description{
    font:0.8em;
    margin:auto;
    padding:5px;
}

.fld{
    width:100%;
}

select{
    width: 60%;
    height: 2.6em;
}

input{
    width:60%;
    border-radius:4px;
    line-height:2.2;
}

label{
    color:#fff;
    font-size:1.4em;
    line-height:2.2;
    width:35%;
}

#date{
    line-height:2.2;
}

.submit{
    width: 209px;
    height: 2.5em;
    margin-left:45%;
    border: 1px solid chartreuse;
    border-radius: 5px;
    background-color: rgba(255, 255, 255, 0.3);
}

</style>