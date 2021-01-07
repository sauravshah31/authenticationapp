<div class="section">
<h2>Authentication using Flask REST API</h2>
<hr/>
<div class="content">
    <h3>API End points</h3>
    <h4>/api/login</h4>
    <code>
        <b>Methods</b> : POST <br/><br/>
        <b>Request Data</b>: <br/>
            name : username / email of the user  <br/>
            password : password of the user <br/><br/>
        <b>Response Data</b>:<br/>
            <mark>Status 200:</mark><br/>
                token: jwt token<br/>
                user_name : username of the logged in user<br/>
                email : email of the logged in user<br/>
            <mark>Status Others</mark><br/>
                description: description of the error<br/>
    </code>
    <h4>/api/register</h4>
    <code>
        <b>Methods</b> : POST <br/><br/>
        <b>Request Data</b>: <br/>
            user_name : username of the user  <br/>
            email:email of the user <br/>
            password : password of the user <br/><br/>
        <b>Response Data</b>:<br/>
            <mark>Status 200:</mark><br/>
                success: true<br/>
                message : New user created<br/>
            <mark>Status Others</mark><br/>
                description: description of the error<br/>
    </code>
    <h4>/api/logout</h4>
    <code>
        <b>Methods</b> : GET <br/><br/>
        <b>Request Header</b>: <br/>
            x-access-token : jwt access token  <br/>
        <b>Response Data</b>:<br/>
            <mark>Status 200:</mark><br/>
                success: true<br/>
                message : Logged out<br/>
            <mark>Status Others</mark><br/>
                description: description of the error<br/>
    </code>
    <h4>/api/verify</h4>
    <code>
        <b>Methods</b> : GET <br/><br/>
        <b>Request Header</b>: <br/>
            x-access-token : jwt access token  <br/>
        <b>Response Data</b>:<br/>
            <mark>Status 200:</mark><br/>
                user_name: username of current user<br/>
                email : email of current user<br/>
            <mark>Status Others</mark><br/>
                description: description of the error<br/>
    </code>
</div>