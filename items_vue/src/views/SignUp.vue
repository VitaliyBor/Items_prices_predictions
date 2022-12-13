<template>
    <div class="page-sign-up">
        <div class="columns">
            <div class="column is-4 is-offset-4" style="background-color: #ffffff;border-radius: 10px;padding: 20px;">
                <h1 class="title">Реєстрація</h1>

                <form @submit.prevent="submitForm">
                    <div class="field">
                        <label>Ім'я</label>
                        <div class="control">
                            <input type="text" class="input" v-model="username">
                        </div>
                    </div>

                    <div class="field">
                        <label>Пароль</label>
                        <div class="control">
                            <input type="password" class="input" v-model="password">
                        </div>
                    </div>

                    <div class="field">
                        <label>Повторіть пароль</label>
                        <div class="control">
                            <input type="password" class="input" v-model="password2">
                        </div>
                    </div>
                    
                    <!-- <p> Вкажіть свою вікову группу</p>
                     <div class="select ">
                       <select v-model="age">
                         <option disabled> Вікова группа </option>
                         <option>18-25 років</option>
                         <option>26-30 років</option>
                         <option>31-40 років</option>
                         <option>41-50 років</option>
                         <option>5</option>
                       </select>
                     </div>

                      <p> Свій середній дохід </p>
                     <div class="select ">
                       <select v-model="sallary">
                         <option disabled>Заплата середня</option>
                         <option>6-8 тисяч гривень</option>
                         <option>2</option>
                         <option>3</option>
                         <option>4</option>
                         <option>5</option>
                       </select>
                     </div>

                      <p> Ваша стать </p>
                     <div class="select ">
                       <select v-model="sex">
                         <option disabled>Ваша стать</option>
                         <option>чоловіча</option>
                         <option>2</option>
                       </select>
                     </div> -->


                    <div class="notification is-danger" v-if="errors.length">
                        <p v-for="error in errors" v-bind:key="error">Щось пішло не так. Переконайтеся в тому, що паролі співпадають, ваш пароль більше 8 символів та те, що він містить не тільки цифри</p>
                    </div>

                    <div class="field">
                        <div class="control">
                            <button class="button is-dark">Зареєструватися</button>
                        </div>
                    </div>

                    <hr>

                    Або  <router-link to="/log-in"> авторизуйтеся </router-link> !
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'

export default {
    name: 'SignUp',
    data() {
        return {
            username: '',
            password: '',
            password2: '',
            age:'1',
            sallary:'1',
            sex:'1',
            errors: []
        }
    },
    methods: {
        submitForm() {
            this.errors = []

            if (this.username === '') {
                this.errors.push('The username is missing')
            }

            if (this.password === '') {
                this.errors.push('The password is too short')
            }

            if (this.password !== this.password2) {
                this.errors.push('The passwords doesn\'t match')
            }

            if (!this.errors.length) {

                let userAge =  1;
                let avarageSallary = 1;
                let sexPerson = 1;
                console.log(''+userAge+avarageSallary+sexPerson)

                const formData = {
                    username: this.username,
                    password: this.password,
                    user_age: userAge,
                    user_sallary: avarageSallary,
                    user_sex: sexPerson
                }

                axios
                    .post("/api/v1/users/", formData)
                    .then(response => {
                        toast({
                            message: 'Account created, please log in!',
                            type: 'is-success',
                            dismissible: true,
                            pauseOnHover: true,
                            duration: 2000,
                            position: 'bottom-right',
                        })

                        this.$router.push('/log-in')
                    })
                    .catch(error => {
                        if (error.response) {
                            for (const property in error.response.data) {
                                this.errors.push(`${property}: ${error.response.data[property]}`)
                            }

                            console.log(JSON.stringify(error.response.data))
                        } else if (error.message) {
                            this.errors.push('Something went wrong. Please try again')
                            
                            console.log(JSON.stringify(error))
                        }
                    })
            }
        }
    },
    switchAge(personAge){
        switch(personAge){ 
        case '18-25 років':
            return  1;
        case '26-30 років':
            return  2;
        case '31-40 років':
            return  3;
        case '41-50 років':
            return  4;
        case '51+ років':
            return  5;
        }
    },
      switchSallary(personSallary){
        switch(personSallary){ 
        case '6-8 тисяч гривень':
            return  1;
        case '9-11 тисяч гривень':
            return  2;
        case '12-14 тисяч гривень':
            return  3;
        case '15-20 тисяч гривень':
            return  4;
        case '21+ тисяч гривень':
            return  5;
        }
    },
    switchSex(sexPerson){
        switch(sexPerson){
            case 'чоловіча':
                return getRandomIntInclusive(1,3);
            case 'жіноча':
                return getRandomIntInclusive(4,5);
        }
    },
     getRandomIntInclusive(min, max) {
        min = Math.ceil(min);
        max = Math.floor(max);
        return Math.floor(Math.random() * (max - min + 1)) + min; 
      }
}
</script>