const routes=[
    {path:'/home',component:home},
    {path:'/passengers',component:passengers},
    {path:'/airport',component:airport},
    {path:'/employees',component:employees},
    {path:'/flights',component:flights}

]

const router=new VueRouter({
    routes
})

const app = new Vue({
    router
}).$mount('#app')