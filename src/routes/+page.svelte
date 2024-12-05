<script lang="ts">
	import type { TransactionRowType } from '$lib/app/types';
	import Upload from '$lib/components/Upload.svelte';
	import TransactionTable from '$lib/components/TransactionTable.svelte';
	import { LightSwitch } from '@skeletonlabs/skeleton';

	import { invoke } from '@tauri-apps/api/core';

	let file: String | undefined;
	let transactions: TransactionRowType[] = [];

	const fileUploadHandler = (files: FileList) => {
		file = files.item(0)?.webkitRelativePath;
		invoke('send_csv', { file_path: file });
	};
</script>

<div class="flex flex-col w-screen h-screen">
	<div class="flex justify-start p-4">
		<LightSwitch />
	</div>

	{#if file != null}
		<div class="flex-grow flex flex-col items-center justify-center w-screen mb-4">
			<div class="w-3/4 mb-6">
				<h1 class="text-4xl font-bold">Transactions</h1>
			</div>

			<div class="flex-grow flex justify-center w-screen">
				<TransactionTable data={transactions} />
			</div>
		</div>
	{:else}
		<div class="flex-grow flex justify-center items-center w-screen">
			<Upload fileHandler={fileUploadHandler} />
		</div>
	{/if}
</div>
