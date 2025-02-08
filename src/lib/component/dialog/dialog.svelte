<script>
    let {children, data, config, name, title, onAction} = $props();
    let state = $state(!data
        ? {}
        : !config?.dataToState
            ? {...data}
            : config?.dataToState({...data}))

    $inspect(state,data,config,name,title)
    
    // @ts-ignore
    const onActionHandler = (action, args) => {
        if (config?.action && config.action[action])
        {
            return config.action[action](args, state);
        }
        
        switch (action)
        {
            default: {}
        }
        
        onAction && onAction(action, args);
    }
    const expandLayout = () => {

    };

    const renderField = (field) => {
        console.log({field});
    };
</script>

<div>
    {#if title}
        <h2>{title}</h2>
    {/if}
    
    {#each expandLayout(config.layout) as field}
        {renderField(field)}
    {/each}
</div>

