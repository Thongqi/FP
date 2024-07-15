document.addEventListener('DOMContentLoaded', ()=>{
    // show_post();

    console.log(document.getElementById('newpost'))
    document.getElementById('newpost').onsubmit = submit_post
        
    // $('#newpost').on('submit', function(event){
    //     event.preventDefault();
    //     console.log("form submitted!")
    //     submit_post();
    // })
    
    document.querySelector('#follow').addEventListener('click', e=>follow(e))
    
})

function follow(event){
    data = document.querySelector('#follow').innerHTML
    var follower = parseInt(document.querySelector('#followers').innerHTML)
    console.log(data, typeof follower)
    const csrftoken = document.getElementsByName('csrfmiddlewaretoken')[0].value
    console.log(csrftoken)
    event.preventDefault();
    id = parseInt(document.querySelector('#id').innerHTML)
    fetch(`/profile/${id}/`, {
        headers:{
            'Content-Type':'application/json',
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': csrftoken,
            }, 
        method:'POST',
        body: data,
    })
    //.then(response=>response.json())
    .then(data => {
        console.log(data)
        selector = document.getElementById('follow')
        if (selector.innerHTML == 'Following'){
            selector.innerHTML = 'Follow'
            follower--;
            document.querySelector('#followers').innerHTML = follower

        }
        else {
            selector.innerHTML = 'Following'
            follower++;
            document.querySelector('#followers').innerHTML = follower
        }
        
    })
    .catch(error => {
        console.log(error)
        console.error('Error:', error);
    })
    //set Timeout(window.location, 100)
    // $.ajax({
    //     type:'POST',
    //     url: '{% url "profile" %}',
    //     data:
    //     {
    //         'operation': $(this).innerHTML,
    //         'csrfmiddlewaretoken': '{{ csrf_token }}'
    //     },
    //     success: function(){
    //         console.log(response)
    //         selector = document.getElementById('follow')
    //         if (operation == 'Following'){
    //             selector.innerHTML = 'Follow'
    //         }
    //         else {
    //             selector.innerHTML = 'Following'
    //         }
            
            
    //     }
    // })
}






function submit_post(event){
    const addpost = document.querySelector('#id_post')
    console.log(addpost.value)
    event.preventDefault()
    // const newpostForm = document.querySelector('#newpost')
    // //on submit form

    // // console.log("working")
    // // $.ajax({
    // //     url: '/',
    // //     type: 'POST',
    // //     data:{ the_post: $('#id_post').val()},

    // //     success: function(json){
    // //         $('#id_post').val('');
    // //         console.log(json);
    // //         console.log('success')
    // //     }
    // // })
    
    fetch('', {
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':document.getElementsByName('csrfmiddlewaretoken')[0].value,
        },
        mode: 'same-origin',
        body:JSON.stringify({
            addpost: addpost.value
        })
    })
    .then(response => response.json())
    .then(result => {

        console.log(result);
        result.post.forEach(item=>{
            const posts = document.createElement('div');

            const user = document.createElement('div')
            user.innerHTML = document.get

            const body = document.createElement('div')
            body.innerHTML = item['post']

            const time = document.createElement('div')
            time.innerHTML = item['createdOn']

            

            posts.appendChild(user)
            posts.appendChild(body)
            posts.appendChild(time)
            //posts.appendChild(button)
            posts.classList.add('post')
            posts.id= `${post}.id`

            document.querySelector('#show_posts').appendChild(posts)
        })
        
    })
    //clear user input after submit
    addpost.value = '';
    // document.querySelector('#show_posts').innerHTML = ''
    // setTimeout(show_post, 100)

}

function show_post(){
   
    fetch('/allposts', {
        headers:{
            'Content-Type':'application/json',
            'X-Requested-With': 'XMLHttpRequest',
            }, 
    })
    .then(response=>response.json())
    .then(data => {
        console.log(data)
        data.posts.forEach(post => {
            console.log(post);

            const posts = document.createElement('div');

            const user = document.createElement('div')
            user.innerHTML = post['id']

            const body = document.createElement('div')
            body.innerHTML = post['post']

            const time = document.createElement('div')
            time.innerHTML = post['modifiedOn']

            const button = document.createElement('button')

            // button.addClass('fa-solid fa-heart')

            posts.appendChild(user)
            posts.appendChild(body)
            posts.appendChild(time)
            posts.appendChild(button)
            posts.classList.add('post')
            posts.id= `${post}.id`

            document.querySelector('#show_posts').appendChild(posts)
            
        });
    })

    
}