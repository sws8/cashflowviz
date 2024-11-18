<script lang="ts">
	import type { TransactionRowType } from '$lib/app/types';
	import TransactionRow from './TransactionRow.svelte';
	export let data: TransactionRowType[] = [];
</script>

<div class="table-container w-3/4">
	<!-- Native Table Element -->
	<table class="table table-hover">
		<thead>
			<tr>
				<th>Account Type</th>
				<th>Account Number</th>
				<th>Transaction Date</th>
				<th>Cost</th>
				<th>Description</th>
				<th>Category</th>
			</tr>
		</thead>
		<tbody>
			{#each data as row}
				<TransactionRow data={row} />
			{/each}
		</tbody>
	</table>
</div>
