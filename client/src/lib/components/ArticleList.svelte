<script>
    import { Link } from "svelte-routing";
    import {getArticleList} from "../api/article";
</script>

{#await getArticleList()}
    <p>loading...</p>
{:then articles}
    <ul>
        {#each articles as { link, title }}
            <li>
                <Link to="/article/{link}">
                    {title}
                </Link>
            </li>
        {/each}
    </ul>
{:catch error}
    <p style="color: red">{error.message}</p>
{/await}
