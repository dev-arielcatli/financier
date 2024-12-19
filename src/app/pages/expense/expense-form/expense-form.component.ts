import { Component, inject } from '@angular/core';
import { FormBuilder, ReactiveFormsModule } from '@angular/forms';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { Expense } from '../expense.model';
import { MatDialogActions, MatDialogContent } from '@angular/material/dialog';
import { MatButtonModule } from '@angular/material/button';

@Component({
  selector: 'fn-expense-form',
  imports: [
    ReactiveFormsModule,
    MatFormFieldModule,
    MatInputModule,
    MatDialogActions,
    MatButtonModule,
  ],
  templateUrl: './expense-form.component.html',
  styleUrl: './expense-form.component.scss',
})
export class ExpenseFormComponent {
  private formBuilder = inject(FormBuilder);

  expenseForm = this.formBuilder.group<Expense>({
    id: '',
    name: '',
    description: '',
    quantity: 0,
    amount: 0,
    date: new Date(),
    createdAt: new Date(),
    updatedAt: new Date(),
    address: '',
    tags: [],
  });
}
