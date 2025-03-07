<script>
	import ArticleList from "../lib/components/ArticleList.svelte";
	import {getArticle} from "../lib/api/article";
	import { marked } from "marked";
	const {id} = $props()
</script>

<div class="container">
	<div class="main">
		{#await getArticle(id)}
			<h1>Article</h1>
			<p>Loading</p>
		{:then article}
			<h1>{article.title}</h1>
			<div>{@html marked.parse(article.content)}</div>
		{:catch error}
			<p style="color: red">{error.message}</p>
		{/await}
	</div>
	<div class="aside">
		<img src="/balaton-beach.jpg" style="width:100%;"/>
		<h2>Other articles</h2>
		<ArticleList />
	</div>
</div>

<style>
	.container {
		display: flex;
		align-items: flex-start;
	}
	.main {
		flex: 9;
	}
	.aside {
		flex: 3;
	}
</style>
