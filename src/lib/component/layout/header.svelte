<script>
    let {currentPath} = $props();

    const routes = [
        {
            href:"/",
            label:"Home"
        },
        {
            href:"/blog",
            label:"Blog"
        },
        {
            href:"/about",
            label:"About"
        },
        {
            href:"/contact",
            label:"Contact"
        }
    ];
</script>

<div class={currentPath==='/' ? "homepage" : "routepage"}> 
    <header  class="container">
        <h1 class="item">Andrea</h1>
        <nav>
            {#each routes as {href, label}}
                <a {href} class={href===currentPath ? "current" : undefined} >
                    {label}
                </a>        
            {/each}
        </nav>
    </header>

</div>
<style>
    .container {
        display: flex;
        justify-content: space-evenly;
            align-items: center;
    }
    .item {
        size: 2;
    }
    nav{
        background:#def;
        color:#666;
        z-index:2;
        height: 5vh;
        border-radius:var(--border-radius);
        font-size: 2.5vh;
        gap:1em;
        margin:-1vh auto 1vh;
        padding:1vh;
        display:flex;
        position:relative;
        width:fit-content;
        opacity: 50%;
    }
    nav a{
        text-decoration:none
    }
    nav .current{
        border-bottom:2px solid
    }    
    .homepage {
        margin-top: 40vh;
        position: sticky;
        top: 0;
        z-index: 9999
    }
    .routepage {
        margin-top: 0vh;
        position: sticky;
        top: 0;
        z-index: 9999
    }
    header {
        background-color: #666;
        border-radius:var(--border-radius);
        text-align: center;
        font-size: 6vh;
        color: #def;
        opacity: 80%;
        position: sticky;
        height: 20vh
        top: 0;
    }
</style>
