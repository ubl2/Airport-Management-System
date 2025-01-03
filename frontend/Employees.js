const employees={
	template:`
	<div>
	<h3>User Cannot Edit Employee Details</h3>
	<table class="table table-striped">
		<thead>
			<tr>
				<th>
					SSN
				</th>
				<th>
					Employee ID
				</th>
				<th>
					Joining Date
				</th>
				<th>
					Airport ID
				</th>
				<th>
					Job Name
				</th>
			</tr>
		</thead>
		<tbody>
			<tr v-for="dep in employees">
				<td>{{dep.SSN}}</td>
				<td>{{dep.employee_ID}}</td>
				<td>{{dep.joining_date}}</td>
				<td>{{dep.airport_ID}}</td>
				<td>{{dep.job_name}}</td>
		</tr>
	</tbody>

</table>
</div>
`,
data(){
	return{
		employees:[],
		modalTitle:"",
		SSN:0,
		employee_ID:"",
		joining_date:"",
		airport_ID:"",
		job_name:"",
		flag:0
	}
},
methods:{
	refreshData(){
		axios.get(variables.APIurl+"employees")
		.then((response)=>{
			this.employees=response.data;
		});
	},
},
mounted:function(){
	this.refreshData();
}
}