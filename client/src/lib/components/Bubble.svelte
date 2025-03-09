<script>
    const {children, background="darkgrey"} = $props();
</script>
<hgroup class="speech-bubble" style='--bg:{background};'>
	{@render children()}
</hgroup>

<style>
    .speech-bubble {
        position: relative;
        background: var(--bg);
        border-radius: .4em;
    }

    .speech-bubble:after {
        content: '';
        position: absolute;
        bottom: 0;
        left: 50%;
        width: 0;
        height: 0;
        border: 1.531em solid transparent;
        border-top-color: var(--bg);
        border-bottom: 0;
        border-left: 0;
        margin-left: -0.766em;
        margin-bottom: -1.531em;
    }
</style>