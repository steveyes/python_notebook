window.onload = function () {
    var data = {
        message: "Hi Vue!",
        msg: "kk",
        checkedNames: ['Jack', 'John'],
        picked: "Two",
        a: 'before change',
        rawHtml: 'Using v-html directive: <span style="color:red">this should be red</span>',
        color: 'blue',
        number: 10,
        ok: false,
        seen: false,
        url: 'https://www.google.com',
        isActive: true,
        isGreen: true,
        size: '50px',
        type: 'A',
        items: [
            {message: 'Foo'},
            {message: 'Bar'}
        ],
        object: {
            title: 'How to do lists in Vue',
            author: 'Jane Doe',
            publishedAt: '2020-10-12'
        },
        counter: 0,
        name: "Vue"
    };
    var methods = {
        click1: function () {
            console.log('click1');
        },
        click2: function () {
            console.log('click2');
        },
        greet: function (str, e) {
            alert(str);
            console.log(e);
        },
        submit: function () {
            console.log(this.picked);
        },
        clicknow: function (e) {
            console.log(e);
        }
    };

    Vue.component('button-counter', {
        props: ['title'],
        data: function () {
            return {
                count: 0
            }
        },
        template: '<div><h1>Hi...</h1><button v-on:click="clickfun">{{ title }}You clicked {{ count }} times.</button><slot></slot></slot></div>',
        methods: {
            clickfun: function () {
                this.count++;
                this.$emit('clicknow', this.count);
            }
        },

    })


    var vm = new Vue({
        el: '#app',
        data: data,
        methods: methods,
        components: {
            test: {
                template: "<h2>h2...</h2>",
            }
        }
    });

    vm.$data.message = "Hello Vue!";
    vm.$watch('a', function (newVal, oldVal) {
        console.log(newVal, oldVal)
    });
    vm.$data.a = "after changed";
}
