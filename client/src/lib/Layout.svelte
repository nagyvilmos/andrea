<script>
	//import { page } from '$app/stores';
	import Header from "./Header.svelte";
	//const path = window.location.pathname;
	let { currentPath, wide, children } = $props();
</script>

<svelte:head>
	<title>Resiliance 4 Health</title>
	<meta name="description" content="Holistic Health Help, resiliance, healthy living, health coach" />
</svelte:head>

<Header {currentPath} />
<div class={wide ? "content wide" : "content"}>
	{@render children()}
</div>

<style>
	div.wide {
		padding: 5vh 16px !important;
	}
	div.content {
		background-color: white;
		border-radius: var(--border-radius);
		border-bottom: 2px solid #abc;
		opacity: 70%;
		margin-top: 8px;
		padding: 5vh 20vw;
	}
</style>
