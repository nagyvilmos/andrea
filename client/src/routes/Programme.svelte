<script>
  import Disk from "../lib/components/Disk.svelte";
  const items = [
    { id: 0, label: "Essentials" },
    { id: 1, label: "Signature" },
    { id: 2, label: "VIP" },
  ];
  let activeTab = $state(0);

  const handleClick = (tabValue) => () => (activeTab = tabValue);
</script>

<h1>Programmes and Packages</h1>

<div class="container">
  <div class="main">
    <!-- Make this three tabs -->

    <ul class="tab">
      {#each items as item}
        <li class={activeTab === item.id ? "active tabitem" : "tabitem"}>
          <span on:click={handleClick(item.id)}>{item.label}</span>
        </li>
      {/each}
    </ul>

    <div class="box" hidden={activeTab !== 0}>
      <div class="package">
        <div class="detail">
          <ul>
            <li>Initial personal consultation - 90 minute</li>
            <li>Five 1-to-1 50-minute weekly coaching sessions</li>
            <li>Whatsup contact from Monday to Friday 8-5</li>
            <li>Unlimited email contact – response in max 24 hour</li>
            <li>
              Extra laser coaching – max 3 15-minute session for the first three
              weeks
            </li>
            <li>Resources – client hands-out</li>
          </ul>
          <p>Cost: £360</p>
        </div>
        <Disk main={6} sub="sessions" background="coral" />
      </div>
    </div>

    <div class="box" hidden={activeTab !== 1}>
      <div class="package">
        <div class="detail">
          <ul>
            <li>Initial personal consultation - 90 minute</li>
            <li>Five 1-to-1 50-minute weekly coaching sessions</li>
            <li>Whatsup contact from Monday to Friday 8-5</li>
            <li>Unlimited email contact – response in max 24 hour</li>
            <li>
              Extra laser coaching – max 3 15-minute session for the first three
              weeks
            </li>
            <li>Resources – client hands-out</li>
          </ul>
          <p>Cost: £500</p>
        </div>
        <Disk main={9} sub="sessions" background="silver" />
      </div>
    </div>

    <div class="box" hidden={activeTab !== 2}>
      <div class="package">
        <div class="detail">
          <ul>
            <li>Initial personal consultation - 90 minute</li>
            <li>Five 1-to-1 50-minute weekly coaching sessions</li>
            <li>Whatsup contact from Monday to Friday 8-5</li>
            <li>Unlimited email contact – response in max 24 hour</li>
            <li>
              Extra laser coaching – max 3 15-minute session for the first three
              weeks
            </li>
            <li>Resources – client hands-out</li>
          </ul>
          <p>Cost: £680</p>
        </div>
        <Disk main={12} sub="sessions" background="goldenrod" />
      </div>
    </div>
  </div>
  <div class="aside">
    <img src="/pomegranite-salad.jpg" style="width:100%;" />
    <img src="/warm-salad.jpg" style="width:100%;" />
  </div>
</div>
<br />

<style>
  .package {
    margin-top: 8px;
    padding: 12px;
    border: 2px solid;
    border-radius: 14px;
    display: flex;
    align-items: flex-start;
  }
  .detail {
    flex: 10;
  }
  .box {
    margin-bottom: 10px;
    padding: 40px;
    border: 1px solid #dee2e6;
    border-radius: 0 0 0.5rem 0.5rem;
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

  .tabitem.active {
    color: #495057;
    background-color: rgb(157, 203, 247);
    border-color: rgb(83, 84, 85) #dee2e6 #fff;
  }
</style>
