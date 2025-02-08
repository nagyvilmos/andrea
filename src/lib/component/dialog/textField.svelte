<script>
    let { state, label, name} = $props();
    $inspect(state, label, name)

</script>

{#if !!label}
<p>{label}</p>
{/if}
<input value={state[name] ?? ""}/>