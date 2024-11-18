<script lang="ts">
	import type { TransactionRowType } from '$lib/app/types';
	import TransactionCategory from './TransactionCategory.svelte';
	export let data: TransactionRowType;
</script>

<tr>
	<td>{data.accountType}</td>
	<td>{data.accountNumber}</td>
	<td>{data.transactionDate}</td>
	<td>{data.cost}</td>
	<td>{data.description}</td>
	<TransactionCategory value={data.category} />
</tr>
