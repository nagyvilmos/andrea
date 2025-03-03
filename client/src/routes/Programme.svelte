<script>
  import Disk from "../lib/components/Disk.svelte";
  const items = [
    {id:0, label:'Essentials'},
    {id:1, label:'signature'},
    {id:2, label:'VIP'}
  ];
  let activeTab = $state(0);

  const handleClick = tabValue => () => (activeTab = tabValue);
</script>

<h1>Programmes and Packages</h1>

<!-- Make this three tabs -->

<ul class='tab'>
{#each items as item}
	<li class={activeTab === item.value ? 'active tabitem' : 'tabitem'}>
		<span on:click={handleClick(item.id)}>{item.label}</span>
	</li>
{/each}
</ul>


<div class="box" hidden={activeTab!==0}>
    <div class="container">
        <div class="main">
            <ul>
                <li>Initial personal consultation - 90 minute</li>
                <li>Five 1-to-1 50-minute weekly coaching sessions</li>
                <li>Whatsup contact from Monday to Friday 8-5</li>
                <li>Unlimited email contact – response in max 24 hour</li>
                <li>Extra laser coaching – max 3 15-minute session for the first three weeks</li>
                <li>Resources – client hands-out</li>
            </ul>
            <p>Cost: £360</p>
        </div>
        <Disk main={6} sub="sessions" />
    </div>
</div>

<div class="box" hidden={activeTab!==1}>
    <div class="container">
        <div class="main">
            <ul>
                <li>Initial personal consultation - 90 minute</li>
                <li>Five 1-to-1 50-minute weekly coaching sessions</li>
                <li>Whatsup contact from Monday to Friday 8-5</li>
                <li>Unlimited email contact – response in max 24 hour</li>
                <li>Extra laser coaching – max 3 15-minute session for the first three weeks</li>
                <li>Resources – client hands-out</li>
            </ul>
            <p>Cost: £600</p>
        </div>
        <Disk main={9} sub="sessions" />
    </div>
</div>

<div class="box" hidden={activeTab!==2}>
    <div class="container">
        <div class="main">
            <ul>
                <li>Initial personal consultation - 90 minute</li>
                <li>Five 1-to-1 50-minute weekly coaching sessions</li>
                <li>Whatsup contact from Monday to Friday 8-5</li>
                <li>Unlimited email contact – response in max 24 hour</li>
                <li>Extra laser coaching – max 3 15-minute session for the first three weeks</li>
                <li>Resources – client hands-out</li>
            </ul>
            <p>Cost: £800</p>
        </div>
        <Disk main={12} sub="sessions" />
    </div>
</div>

<br/>

<style>
    .package {
        margin-top: 8px;
        padding: 12px;
        border: 2px solid;
        border-radius: 14px;
    }
	.container {
		display: flex;
		align-items: flex-start;
	}
	.main {
		flex: 10;
	}
	.aside {
		flex: 2;
        align: center;
	}


	.box {
		margin-bottom: 10px;
		padding: 40px;
		border: 1px solid #dee2e6;
    border-radius: 0 0 .5rem .5rem;
    border-top: 0;
	}
  .tab {
    display: flex;
    flex-wrap: wrap;
    padding-left: 0;
    margin-bottom: 0;
    list-style: none;
    border-bottom: 1px solid #dee2e6;
  }
    .tabitem {
        margin-bottom: -1px;
    }

  span {
    border: 1px solid transparent;
    border-top-left-radius: 0.25rem;
    border-top-right-radius: 0.25rem;
    display: block;
    padding: 0.5rem 1rem;
    cursor: pointer;
  }

  span:hover {
    border-color: #e9ecef #e9ecef #dee2e6;
  }

  .tabitem.active > span {
    color: #495057;
    background-color:#efg;
    border-color: #dee2e6 #dee2e6 #fff;
  }

</style>