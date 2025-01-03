const flights={
	template:`
	<div>
		<h3>User cannot edit Flight Details</h3>
	<table class="table table-striped">

		<thead>
			<tr>
				<th>
					Flight ID
				</th>
				<th>
					Status
				</th>
				<th>
					Tme At Source
				</th>
				<th>
					Time At Destination
				</th>
				<th>
					Duration
				</th>
				<th>
					Source City
				</th>
				<th>
					Destination City
				</th>
				<th>
					Source Airport ID
				</th>
				<th>
					Airline ID
				</th>
				<th>
					Connection ID
				</th>
				<th>
					Options
				</th>
			</tr>
		</thead>
		<tbody>
			<tr v-for="dep in flights">
				<td>{{dep.flight_ID}}</td>
				<td>{{dep.status}}</td>
				<td>{{dep.time_at_source}}</td>
				<td>{{dep.time_at_destination}}</td>
				<td>{{dep.duration}}</td>
				<td>{{dep.source}}</td>
				<td>{{dep.destination}}</td>
				<td>{{dep.source_airport_ID}}</td>
				<td>{{dep.airline_ID}}</td>
				<td>{{dep.connection_ID}}</td>
				<td>
					<button type="button" class="btn btn-light mr-1">
						<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-pencil-square" viewBox="0 0 16 16">
							<path d="M15.502 1.94a.5.5 0 0 1 0 .706L14.459 3.69l-2-2L13.502.646a.5.5 0 0 1 .707 0l1.293 1.293zm-1.75 2.456-2-2L4.939 9.21a.5.5 0 0 0-.121.196l-.805 2.414a.25.25 0 0 0 .316.316l2.414-.805a.5.5 0 0 0 .196-.12l6.813-6.814z"/>
							<path fill-rule="evenodd" d="M1 13.5A1.5 1.5 0 0 0 2.5 15h11a1.5 1.5 0 0 0 1.5-1.5v-6a.5.5 0 0 0-1 0v6a.5.5 0 0 1-.5.5h-11a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 .5-.5H9a.5.5 0 0 0 0-1H2.5A1.5 1.5 0 0 0 1 2.5v11z"/>
						</svg>
						<button type="button" class="btn btn-light mr-1">
							<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-trash-fill" viewBox="0 0 16 16">
								<path d="M2.5 1a1 1 0 0 0-1 1v1a1 1 0 0 0 1 1H3v9a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2V4h.5a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1H10a1 1 0 0 0-1-1H7a1 1 0 0 0-1 1H2.5zm3 4a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7a.5.5 0 0 1 .5-.5zM8 5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7A.5.5 0 0 1 8 5zm3 .5v7a.5.5 0 0 1-1 0v-7a.5.5 0 0 1 1 0z"/>
							</svg>
						</button>
					</button>
				</td>
			</tr>
		</tbody>

	</table>
</div>
	`,
	data(){
		return{
			flights:[]
		}
	},
	methods:{
		refreshData(){
			axios.get(variables.APIurl+"flights")
			.then((response)=>{
				this.flights=response.data;
			});
		}
	},
	mounted:function(){
		this.refreshData();
	}
}