<script>
    import { Link } from "svelte-routing";

    let { currentPath } = $props();
    //console.debug({ currentPath });
    const routes = [
        {
            href: "/",
            label: "Home",
        },
        {
            href: "/about",
            label: "My Story",
        },
        {
            href: "/programme",
            label: "Programmes",
        },
        {
            href: "/article",
            label: "Articles",
            hidden: false,
        },
        {
            href: "/contact",
            label: "Contact",
            hidden: true,
        },
    ].filter((i) => !i.hidden);
</script>

<!-- <div class={currentPath === "/" ? "home header" : "header"}> -->
<div class="header">
    <header class="container">
        <h1 class="item">Resiliance 4 Health</h1>
        <nav class="item">
            {#each routes as { href, label }}
                <Link
                    to={href}
                    class={href === currentPath ? "current" : "link"}
                >
                    {label}
                </Link>
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
        font-family: var(--font-script);
        size: 2;
    }
    nav {
        background: #def;
        color: #666;
        z-index: 2;
        height: 5vh;

        border-radius: var(--border-radius);
        font-size: 2.5vh;
        gap: 1em;
        margin: -1vh auto 1vh;
        padding: 1vh;
        display: flex;
        position: relative;
        width: fit-content;
        opacity: 50%;
    }
    .link {
        text-decoration: none;
    }
    .current {
        text-decoration: none;
        border-bottom: 2px solid;
    }
    .header {
        margin-top: 0vh;
        position: sticky;
        top: 0;
        z-index: 9999;
    }
    header {
        background-color: #666;
        border-radius: var(--border-radius);
        text-align: center;
        font-size: 6vh;
        color: #def;
        /* opacity: 80%; */
        position: sticky;
        /* height: 15vh; */
        top: 0;
        padding: 8px;
    }
    h1 {
        font-family: var(--font-script);
        font-size: 64px;
    }
</style>
