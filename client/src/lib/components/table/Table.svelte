<script lang="js">
    const { data, config } = $props();

    const columnList = () => {
        let cols = config?.columns;
        if (!cols) {
            cols = !data
                ? []
                : Object.keys(data[0] ?? []).map((id) => ({ id, sort: null }));
        }
        if (config.showIndex) {
            cols = [
                {
                    id: "_index",
                    label: "",
                    sort: null,
                    render: (_, i) => i + 1,
                },
                ...cols,
            ];
        }
        return cols;
    };

    const columns = $derived(columnList());

    let sort = $state(config.sort ?? {});
    let filter = $state(config.filter ?? []);

    // helper move empty sorted columns to the end.
    const emptyLast = (sorted) => {
        if (!sort?.col) return sorted;
        return [
            ...sorted.filter((r) => (r[sort.col] ?? "") !== ""),
            ...sorted.filter((r) => (r[sort.col] ?? "") === ""),
        ];
    };

    const filteredData = () =>
        filter.length === 0
            ? data
            : data.filter((row) => !filter.find((f) => !f.filter(row)));
    const sortedData = () =>
        emptyLast(
            !sort.col ? filteredData() : filteredData().sort(sort.function),
        );

    const setSort = (id) => {
        const col = columns.find((c) => c.id === id);
        console.log({ id, col });
        if (!col || col.sort === null) {
            sort = { col: undefined };
            return;
        }

        if (sort?.col !== id) {
            sort = { col: id, asc: 1 };
        } else {
            sort = { ...sort, asc: -sort.asc };
        }

        // now create the function:

        let sortFn = col.sort;
        if (sortFn === undefined) {
            console.debug(col.type);
            switch (col.type) {
                case "number": {
                    sortFn = (a, b) => (a[sort.col] ?? 0) - (b[sort.col] ?? 0);
                    break;
                }
                default: {
                    // treat as string
                    sortFn = (a, b) =>
                        (a[sort.col] ?? "").localeCompare(b[sort.col] ?? "");
                    break;
                }
            }
        }
        // if desc reverse the sort
        sort = {
            ...sort,
            function: sort.asc === 1 ? sortFn : (a, b) => -sortFn(a, b),
        };
        console.log({ ...sort });
    };
</script>

<div class="table-container">
    <table>
        <thead>
            <tr>
                {#each columns as column}
                    <td onclick={() => setSort(column.id)}
                        >{column.label ?? column.id}</td
                    >
                {/each}
            </tr>
        </thead>
        <tbody>
            {#each sortedData() as row, index}
                <tr>
                    {#each columns as column}
                        <td>
                            <div class="cell">
                                {!column.render
                                    ? row[column.id]
                                    : column.render(row, index)}
                            </div>
                        </td>
                    {/each}
                </tr>
            {/each}
        </tbody>
    </table>
</div>

<style>
    .table-container {
        padding: 16px;
    }
    table {
        width: 100%;
        border-collapse: collapse;
    }
    thead {
        background-color: #808080;
        color: #080808;
        font-weight: bolder;
    }
    td {
        border: solid black 2px;
    }
    tr {
        min-height: 42px;
    }
    tr:nth-child(even) {
        background-color: #cccccc;
    }
    .cell {
        padding: 4px;
    }
</style>
